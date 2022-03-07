#!/bin/sh

SCRIPT_NAME=`echo $(basename "$0")|sed 's/\.sh$//'`
SCRIPT_DIR=$(dirname "$0")
SCRIPT_DIR=`realpath $SCRIPT_DIR`
# Assuming this script is in taipy-doc/tools
ROOT_DIR=`realpath $SCRIPT_DIR/..`
TOP_DIR=`realpath $SCRIPT_DIR/../..`

usage()
{
    echo "Usage: $SCRIPT_NAME [-h|--help]"
    echo "Locally installs (in tools) the source code of Taipy from different"
    echo "repositories in order to allow the local generation of the"
    echo "documentation set."
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
done

if [ -d $ROOT_DIR"/taipy" ]; then
    echo Removing legacy \'taipy\'
    rm -rf $ROOT_DIR"/taipy"
    mkdir $ROOT_DIR"/taipy"
fi
for m in $MODULES; do
    echo Updating module $m
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
done
echo "Adding taipy's __init__.py"
echo "from taipy.core import *" >$ROOT_DIR/taipy/__init__.py
echo "import taipy.gui as gui" >>$ROOT_DIR/taipy/__init__.py
