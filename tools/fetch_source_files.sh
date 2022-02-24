#!/bin/sh

SCRIPT_NAME=`echo $(basename "$0")|sed 's/\.sh$//'`
SCRIPT_DIR=$(dirname "$0")
SCRIPT_DIR=`realpath $SCRIPT_DIR`
# Assuming this script is in taipy-doc/tools
TOP_DIR=`realpath $SCRIPT_DIR/../..`

usage()
{
    echo "Usage: $SCRIPT_NAME [-h|--help]"
    echo "Locally installs the source code of Taipy from different repositories"
    echo "in order to allow the local generation of the documentation set."
    echo "You can then run 'mkdocs serve'"
}

MODULES="taipy-core taipy-gui"
while [ "$1" != "" ]; do
    case $1 in
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
    if [ $m == "taipy-gui" ] && [ ! -d $TOP_DIR/taipy-gui/taipy/gui/webapp ]; then
	echo "Error: Web app has not been generated in taipy-gui"
	echo "Please:"
	echo "  cd $TOP_DIR/taipy-gui/gui"
	echo "  npm install"
	echo "  npm run build"
	echo "then re-run"
	exit 1

    fi
done

if [ -d taipy ]; then
    echo Removing legacy \'taipy\'
    rm -rf taipy
    mkdir taipy
fi
for m in $MODULES; do
    echo Updating module $m
    (cd $TOP_DIR/$m; \
     tar cf - `find taipy -name \\*.py`) | tar xf -
    if [ $m == "taipy-gui" ]; then
	if [ -d taipy ]; then
	    echo Removing legacy \'gui\'
	    rm -rf gui
	fi
	(cd $TOP_DIR/$m;tar cf - gui/doc) | tar xf -
    fi
done
