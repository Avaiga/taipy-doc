The previous section on [Scalar properties](scalar_props.md) shows how to create a dynamic element
that holds a scalar value. However, when dealing with collections of data, such as tabular data, we
need a more complex approach to support arrays or tables that can be dynamically updated.

In Taipy GUI, tabular data can also be bound to Python variables or expressions, allowing the user
interface to instantly reflect any changes in the underlying data. Custom elements that manage
tabular data must declare their properties to specify the type of data they support, similar to
scalar properties, but now using a structure suitable for collections.
This is handled by the PropertyType class, where you can define the type as an array or table
format, enabling the binding of multidimensional data.

For example, the *data* property of a `table` control can be bound to a two-dimensional array or a
list of objects. When the bound data changes, the table control automatically updates to reflect the
new content in the user interface.<br/>
This functionality is implemented using the React library, which dynamically generates HTML for the
tabular display. By leveraging Taipy GUI's variable binding capabilities, developers can efficiently
update and manage tabular data in the user interface.

Even if a custom element does not need to update its tabular data dynamically, it can still be
implemented as a dynamic element to take advantage of the expressivity and flexibility offered by
this approach.

# Using tabular data

In this section, we will expand the dynamic element library, initially created in the
[Scalar properties](scalar_props.md) section, by adding a new dynamic custom element.

This dynamic element will accept a property containing tabular data and display it within a table.
When a Python variable is bound to this property, updates to the variable will immediately reflect
in the table content shown on the page, ensuring real-time synchronization.

## Declaring a dynamic element {data-source="gui/extension/example_library/example_library.py#L36"}
Starting from the code mentioned above, here is how you would declare this new element:
```py   title="example_library.py"
from taipy.gui.extension import Element, ElementLibrary, ElementProperty, PropertyType

class ExampleLibrary(ElementLibrary):
    def __init__(self) -> None:
        # Initialize the set of visual elements for this extension library
        self.elements = {
            "game_table": Element(
                "data",
                {
                    "data": ElementProperty(PropertyType.data),
                },
                # The name of the React component (GameTable) that implements this custom
                # element, exported as GameTable in front-end/src/index.ts
                # react_component="GameTable",
            ),
        }
```
The declaration of this dynamic element is very similar to what we created in the
[Scalar properties](scalar_props.md).

The detailed explanation of the code is as follows:

- The *game_table* element includes a single property: *data*.
- The *data* property has the type *PropertyType.data*, meaning it holds a data value and is
  dynamic.
- The *get_name()* method in the *ExampleLibrary* class returns the name of the library as a string.
  This name is used to identify the library within the Taipy GUI framework.
- The *get_elements()* method in the *ExampleLibrary* class returns a dictionary of all elements
  that are part of this library. Each element is defined with its properties and associated React
  component.

## Creating the React component {data-source="gui/extension/example_library/front-end/src/GameTable.tsx"}

The React component for the *game_table* element is defined as follows:

```jsx title="GameTable.tsx" linenums="1"
import React, { useEffect, useMemo, useState } from "react";
import {
    createRequestDataUpdateAction,
    useDispatch,
    useDispatchRequestUpdateOnFirstRender,
    useModule,
    TaipyDynamicProps,
    TableValueType,
    RowType,
    RowValue,
} from "taipy-gui";

interface GameTableProps extends TaipyDynamicProps {
    data: TableValueType;
}

const pageKey = "no-page-key";

const GameTable = (props: GameTableProps) => {
    const { data, updateVarName = "", updateVars = "", id } = props;
    const [value, setValue] = useState<Record<string, Array<RowValue>>>({});
    const dispatch = useDispatch();
    const module = useModule();
    const refresh = data?.__taipy_refresh !== undefined;
    useDispatchRequestUpdateOnFirstRender(dispatch, id, module, updateVars);

    const colsOrder = useMemo(() => {
        return Object.keys(value);
    }, [value]);

    const rows = useMemo(() => {
        const rows: RowType[] = [];
        if (value) {
            Object.entries(value).forEach(([col, colValues]) => {
                    colValues.forEach((val, idx) => {
                        rows[idx] = rows[idx] || {};
                        rows[idx][col] = val;
                    });
            });
        }
        return rows;
    }, [value]);

    useEffect(() => {
        if (refresh || !data || data[pageKey] === undefined) {
            dispatch(
                createRequestDataUpdateAction(
                    updateVarName,
                    id,
                    module,
                    colsOrder,
                    pageKey,
                    {},
                    true,
                    "ExampleLibrary",
                ),
            );
        } else {
            setValue(data[pageKey]);
        }
    }, [refresh, data, colsOrder, updateVarName, id, dispatch, module]);

    return (
        <div>
            <table border={1} cellPadding={10} cellSpacing={0}>
                <tbody>
                    {rows.map((row, index) => (
                        <tr key={"row" + index}>
                            {colsOrder.map((col, cidx) => (
                                <td key={"val" + index + "-" + cidx}>{row[col]}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default GameTable;
```

The detailed explanation of the code is as follows:

- We use the [`useDispatch()`](../../../../refmans/reference_guiext/functions/useDispatch.md) hook
  to dispatch actions to the store and initiate backend communications.
- Additionally, the [`useModule()`](../../../../refmans/reference_guiext/functions/useModule.md)
  hook retrieves the page module, enabling correct execution of backend functions.
- To request an update for every dynamic property of an element on initial render, we use the
  [`useDispatchRequestUpdateOnFirstRender()`](../../../../refmans/reference_guiext/functions/useDispatchRequestUpdateOnFirstRender.md)
  hook provided by the Taipy GUI Extension API. This hook takes five parameters:
  - *dispatch*: The React dispatcher associated with the context.
  - *id*: The identifier of the element.
  - *context*: The execution context.
  - *updateVars*: The content of the *updateVars* property.
- We also dispatch the
  [`createRequestDataUpdateAction()`](../../../../refmans/reference_guiext/functions/createRequestDataUpdateAction.md)
  hook to create a request data update action, which updates the context by invoking the
  `(ElementLibrary.)get_data()^` method of the backend library. This invocation triggers an update
  of front-end elements holding the data.

The [`createRequestDataUpdateAction()`](../../../../refmans/reference_guiext/functions/createRequestUpdateAction.md)
hook accepts eight parameters:

- *name*: The name of the variable containing the requested data, as received in the property.
- *id*: The identifier of the visual element.
- *context*: The execution context.
- *columns*: The list of column names required by the element emitting this action.
- *pageKey*: The unique identifier for the data received from this action.
- *payload*: The payload, specific to the component type (e.g., table, chart).
- *allData*: A flag indicating if all the data is requested.
- *library*: The name of the extension library.

## Exporting the React component {data-source="gui/extension/example_library/front-end/src/index.ts"}

When the component is entirely defined, it must be exported by the JavaScript library.
This is done by adding the export directive in the file *<project dir>/<package dir>front-end/src/index.ts*.

```js title="index.ts"
import GameTable from "./GameTable";

export { GameTable };
```

## Using the element {data-source="gui/extension/table_chess_game.py"}

In the example below, we use the *game_table* element to display a chess game board.
The data is represented as a two-dimensional list of strings, where each string represents a chess
piece.<br/>
The board is displayed in a table format using the *game_table* element.<br/>
We can see how the data property of the control is bound to the Python variable *data*, using the
default property syntax.

```py
data = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
]

page = """
## Chess Game
<|{data}|example.game_table|>
"""
```

When you run this application, the page displays the element like this:

<figure>
    <img src="../chess_game-d.png" class="visible-dark"  width="80%"/>
    <img src="../chess_game-l.png" class="visible-light" width="80%"/>
    <figcaption>Chessboard</figcaption>
</figure>
