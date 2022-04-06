#!/bin/sh

SCRIPT_NAME=`echo $(basename "$0")|sed 's/\.sh$//'`
SCRIPT_DIR=$(dirname "$0")
SCRIPT_DIR=`realpath $SCRIPT_DIR`
# Assuming this script is in taipy-doc/tools
ROOT_DIR=`realpath $SCRIPT_DIR/..`
TOP_DIR=`realpath $SCRIPT_DIR/../..`

usage()
{
    echo "Usage: $SCRIPT_NAME [-h|--help] [-no_pull]"
    echo "Locally installs (in tools) the source code of Taipy from different"
    echo "repositories in order to allow the local generation of the"
    echo "documentation set."
    echo "You can then run 'mkdocs serve'"
    echo
    echo "-no_pull prevents the source repository update."
}

MODULES="taipy-core taipy-gui taipy-getting-started"
NO_PULL=false
while [ "$1" != "" ]; do
    case $1 in
        -no_pull)
            NO_PULL=true
            ;;
        -h | --help)
            usage
            exit
            ;;
    esac
    shift
done

# Check if repositories are accessible
for m in $MODULES; do
    if [ ! -d $TOP_DIR/$m ]; then
        echo "Error: module $m must be cloned next to $SCRIPT_DIR"
        exit 1
    fi
done

if [ -d $ROOT_DIR"/taipy" ]; then
    echo Removing legacy \'taipy\'
    rm -rf $ROOT_DIR"/taipy"
    mkdir $ROOT_DIR"/taipy"
fi
for m in $MODULES; do
    echo Updating module $m
    if [ "$NO_PULL" != true ] ; then
      (cd $TOP_DIR/$m; git pull)
    fi
    (cd $TOP_DIR/$m; git pull)
    if [ $m == "taipy-getting-started" ]; then
        (cd $TOP_DIR/$m;tar cf - step_*) | (cd $ROOT_DIR/docs/getting_started/;tar xf -)
        cp $TOP_DIR/taipy-getting-started/README.md $ROOT_DIR/docs/getting_started/index.md
    else
        (cd $TOP_DIR/$m; \
         tar cf - `find taipy -name \\*.py`) | (cd $ROOT_DIR;tar xf -)
        if [ $m == "taipy-gui" ]; then
            if [ -d $ROOT_DIR"/gui" ]; then
                echo Removing legacy \'gui\'
                rm -rf $ROOT_DIR"/gui"
            fi
            echo Updating doc files for taipy-gui
            (cd $TOP_DIR/$m;tar cf - gui/doc) | (cd $ROOT_DIR;tar xf -)
        fi
    fi
done
echo "Adding taipy's __init__.py"
echo "from .core import *" >$ROOT_DIR/taipy/__init__.py
echo "from .gui import Gui" >>$ROOT_DIR/taipy/__init__.py
