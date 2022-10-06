#!/bin/bash
# See usage() for information.

SCRIPT_NAME=`echo $(basename "$0")|sed 's/\.sh$//'`
SCRIPT_DIR=$(dirname "$0")
SCRIPT_DIR=`realpath $SCRIPT_DIR`
# Assuming this script is in taipy-doc/tools
ROOT_DIR=`realpath $SCRIPT_DIR/..`
TOP_DIR=`realpath $SCRIPT_DIR/../..`

MODULES="config core gui getting-started rest auth enterprise"

list_modules()
{
    echo "${1}Valid module names are:"
    for m in $MODULES; do
        echo "${1}  - $m"
    done
}

usage()
{
    echo "Usage: $SCRIPT_NAME [-h|--help] [-no_pull] [<version>...]"
    echo "Locally copies the source code of Taipy from different places"
    echo "in order to allow the generation of the documentation set."
    echo "After this script has run, you can run 'mkdocs serve'."
    echo ""
    echo "Options:"
    echo "-h,--help: Show this help message."
    echo "-no_pull: Prevents the source repository update (local only)."
    echo ""
    echo "<version>: Sets the version for the whole doc set, or specific modules."
    echo "The <version> parameter can be 'local', 'develop' or a valid version number."
    echo "It can be prefixed with '<module>:', then the version applies only to"
    echo "that module. If that prefix is not present, the version applies to all"
    echo "modules".
    list_modules
    echo "<version> arguments overwrite the previous ones."
    echo "i.e.:"
    ms=("${!MODULE_VERSIONS[@]}")
    m=${ms[0]}
    echo "  '2.0 $m:1.0' will set all versions to 2.0 except for"
    echo "    the '$m' module."
    echo "  '$m:1.0 2.0' will set version 2.0 for all modules."
    echo "If <version> is 'local', the code is retrieved from a directory called"
    echo "'taipy-<module>', above the current directory."
    echo "If <version> is 'develop', the develop branch for the indicated repository"
    echo "is used."
    echo "If <version> is '<Major>.<Minor>', the corresponding branch is used."
    echo "If <version> contains an additional '.<Patch>[.<More>]' fragment, then the"
    echo "corresponding tag is extracted from the '<Major>.<Minor>' branch for that"
    echo "module."
    echo "If any version is not 'local', then the 'git' command must be accessible."
    echo ""
    echo "The default behaviour is to use a local version for all modules."
}

NO_PULL=false

# Initialize all module versions
declare -A MODULE_BRANCH
declare -A MODULE_TAG
for m in $MODULES; do
    MODULE_BRANCH[$m]="local"
    MODULE_TAG[$m]=""
done

RE_MODULEVERSION='^(([A-Za-z-]+):)?([0-9]+)\.([0-9]+)(\.([0-9]+)(\.([0-9A-Za-z_]+))?)?$'
RE_MODULE_NOTVERSION='^(([A-Za-z-]+):)?(local|develop)$'

set_version () {
    if [[ $1 =~ $RE_MODULE_NOTVERSION ]]; then
        mod=${BASH_REMATCH[2]}
        type=${BASH_REMATCH[3]}
        if [ -z "$mod" ]; then
            for m in $MODULES; do
                MODULE_BRANCH[$m]=$type
                MODULE_TAG[$m]=""
            done
        else
            if [ -z "${MODULE_BRANCH[$mod]}" ]; then
                echo "Error: Invalid module name '$mod' in -version parameter: $1" >&2
                list_modules
                exit 1
            fi
            MODULE_BRANCH[$mod]=$type
            MODULE_TAG[$mod]=""
        fi
    elif [[ $1 =~ $RE_MODULEVERSION ]]; then
        mod=${BASH_REMATCH[2]}
        maj=${BASH_REMATCH[3]}
        min=${BASH_REMATCH[4]}
        pat=${BASH_REMATCH[6]}
        mor=${BASH_REMATCH[8]}
        branch="$maj.$min"
        tag=""
        if [[ ! -z "$pat" ]]; then
            tag="$branch.$pat"
            if [[ ! -z "$mor" ]]; then
                tag="$tag.$mor"
            fi
        fi
        if [ -z "$mod" ]; then
            for m in $MODULES; do
                MODULE_BRANCH[$m]=$branch
                MODULE_TAG[$m]=$tag
            done
        else
            if [ -z "${MODULE_BRANCH[$mod]}" ]; then
                echo "Error: Invalid module name '$mod' in -version parameter: $1" >&2
                list_modules
                exit 1
            fi
            MODULE_BRANCH[$mod]=$branch
            MODULE_TAG[$mod]=$tag
        fi
    elif [[ $1 = "MKDOCS" ]]; then
        version=$(grep -Ei 'site_url: https://docs\.taipy\.io/en/(develop|release-[0-9].[0-9])' mkdocs.yml_template | grep -oEi [0-9].[0-9] || echo 'develop')
        set_version $version
    else
        echo "Error: Invalid version in -version parameter: $1" >&2
        exit 1
    fi
}

while [[ ! -z "$1" ]]; do
    case $1 in
        -no_pull)
            NO_PULL=true
            ;;
        -h | --help)
            usage
            exit
            ;;
        -*)
            echo "Error: unknown option '$1'." >&2
            usage
            exit
            ;;
        *)
            set_version $1
            ;;
     esac
    shift
done

for m in $MODULES; do
    version=${MODULE_BRANCH[$m]}
    if [ $version != "local" ]; then
        if ! [ -x "$(command -v git)" ]; then
            echo "Error: cannot run the git command to fetch module '$m'." >&2
            exit 1
        else
            break
        fi
    fi
done

echo "Module versions requested:"
for m in $MODULES; do
    version=${MODULE_BRANCH[$m]}
    if [[ ! -z ${MODULE_TAG[$m]} ]]; then
        version="$version (${MODULE_TAG[$m]})"
    fi
    echo "- $m: $version"
done

# Check if module branches/tags/directory exist
if [ X$GITHUB_TOKEN == X ]; then
    GITROOT="https://github.com/Avaiga/taipy"
else
    GITROOT="https://$GITHUB_TOKEN@github.com/Avaiga/taipy"
fi
for m in $MODULES; do
    branch=${MODULE_BRANCH[$m]}
    if [ $branch == "local" ]; then
        if [ ! -d $TOP_DIR/taipy-$m ]; then
            echo "Error: module $m must be cloned next to $SCRIPT_DIR as 'taipy-$m'"
            exit 1
        fi
    elif [ $branch != "develop" ]; then
        git ls-remote --exit-code --heads ${GITROOT}-${m}.git | grep release/${branch} >/dev/null
        if [ $? != 0 ]; then
            echo "Error: No branch 'release/$branch' in repository 'taipy-$m'." >&2
            exit 1
        fi
        # Check tag
        tag=${MODULE_TAG[$m]}
        if [[ ! -z "$tag" ]]; then
            find_tag=$(git ls-remote -t --refs ${GITROOT}-${m}.git|sed -e 's/^.*\/tags\///'|grep -e "${tag}\$")
            if [ ! -f "$find_tag" ]; then
                echo "Error: No tagged version '$tag' (from 'release/$branch') in repository 'taipy-$m'." >&2
                exit 1
            fi
        fi
    fi
done

# Last setup failed?
if [ -d $ROOT_DIR"/tools/taipy" ]; then
    rm -rf $ROOT_DIR"/tools/taipy"
fi
if [ -d $ROOT_DIR"/taipy" ]; then
    echo Removing legacy \'taipy\'
    rm -rf $ROOT_DIR"/taipy"
    mkdir $ROOT_DIR"/taipy"
fi

copy_module_to_taipy()
{
    srcdir=$2/src
    (cd $srcdir; tar cf - `find taipy -name \\*.py`) | (cd $ROOT_DIR;tar xf -)
}

copy_getting_started()
{
    (cd $1;tar cf - step_* src) | (cd $ROOT_DIR/docs/getting_started/;tar xf -)
    cp $1/index.md $ROOT_DIR/docs/getting_started/index.md
    (cd $ROOT_DIR/docs/getting_started; python $1/generate_notebook.py)
}

copy_gui()
{
    if [ -d $ROOT_DIR"/gui" ]; then
        echo Removing legacy \'gui\'
        # Save node_modules for more efficient local usage
        if [ -d $ROOT_DIR"/gui/node_modules" ]; then
            mv $ROOT_DIR"/gui/node_modules" $ROOT_DIR"/gui_node_modules"
        fi
        rm -rf $ROOT_DIR"/gui"
    fi
    echo Updating doc files for gui
    (cd $1;tar cf - gui/*.md gui/*.json gui/doc gui/src) | (cd $ROOT_DIR;tar xf -)
    if [ -d $ROOT_DIR"/gui_node_modules" ]; then
        mv $ROOT_DIR"/gui_node_modules" $ROOT_DIR"/gui/node_modules"
    fi
}

# Extract the modules code
for m in $MODULES; do
    branch=${MODULE_BRANCH[$m]}
    echo "Updating module $m ($branch)"
    if [ $branch == "local" ]; then
        if [ "$NO_PULL" != true ] ; then
            (cd $TOP_DIR/taipy-$m; git pull)
        fi
        if [ $m == "getting-started" ]; then
            copy_getting_started $TOP_DIR/taipy-getting-started
        else
            copy_module_to_taipy $m $TOP_DIR/taipy-$m
            if [ $m == "gui" ]; then
                copy_gui $TOP_DIR/taipy-gui
            fi
        fi
    else
        if [ $branch != "develop" ] ; then
            branch=release/$branch
        fi
        git clone -b $branch ${GITROOT}-${m}.git $ROOT_DIR/tmp-$m
        tag=${MODULE_TAG[$m]}
        if [[ ! -z "$tag" ]]; then
            (cd $ROOT_DIR/tmp-$m;git checkout tags/$tag)
        fi
        if [ $m == "getting-started" ]; then
            copy_getting_started $ROOT_DIR/tmp-getting-started
        else
            copy_module_to_taipy $m $ROOT_DIR/tmp-$m
            if [ $m == "gui" ]; then
                copy_gui $ROOT_DIR/tmp-gui
            fi
        fi
        rm -rf $ROOT_DIR/tmp-$m
    fi
done

# Manually add the taipy.run() function.
# TODO: Automate this, grabbing the function from the 'taipy' repository,
# so we benefit from potential updates.
cat >>$ROOT_DIR/taipy/__init__.py <<EOF

import typing as t

def run(*apps: t.List[t.Union[Gui, Rest]], **kwargs: t.Dict):
    """Run one or multiple Taipy services.

    A Taipy service is an instance of a class that runs code as a Web application.

    Parameters:
        *apps (List[Union[Gui^, Rest^]]): Services to run. If several services are provided, all the services run simultaneously. If this is empty or set to None, this method does nothing.
        **kwargs: Other parameters to provide to the services.
    """
    pass
EOF
