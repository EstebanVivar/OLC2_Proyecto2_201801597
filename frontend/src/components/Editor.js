import React, { useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import 'codemirror/theme/material.css';
import { Button, Form } from 'react-bootstrap';
// eslint-disable-next-line
import axios from 'axios';

var init = `struct Juguete
name::String;
precio::Int64;
end;

struct Mascota
name::String;
juguete::Juguete;
end;

j = Juguete("peluche",56);
m = Mascota("lucas",j);`

const Editor = () => {
    const [TextEditor, getEditor] = useState(init);
    // eslint-disable-next-line
    const [TextConsole, setConsole] = useState("");

    const getX = async (e) => {
        e.preventDefault();
        await axios
            .post("http://localhost:5000/Editor", { input: TextEditor })
            .then(response => {
                if (response) {
                    console.log(response.data)
                    setConsole(response.data)
                }
            })
    }


    return (
        <Form onSubmit={getX}>
            <div className="container-fluid" style={{ width: 100 + "%", height: 88.2 + "vh" }}>

                <div className=" d-flex justify-content-evenly mb-1">
                    <h3 style={{color:"white" }}>
                        Editor
                    </h3>
                    <Button type='submit' variant="dark">
                        ANALIZAR
                    </Button>
                    <h3 style={{color:"white" }}>
                        Consola
                    </h3>
                </div>

                <div className="row gx-1">
                    <div className="col-md-6 " style={{ width: 50 + "%", height: 83 + "vh" }}>
                        <CodeMirror
                            value={TextEditor}
                            onChange={(v) => {
                                getEditor(v.getValue())
                            }}

                            options={{
                                theme: 'material',
                                mode: 'julia',
                            }}
                        />
                    </div>
                    <div className="col-md-6" style={{ width: 50 + "%", height: 83 + "vh" }}>
                        <CodeMirror
                            value={TextConsole}

                            options={{
                                lineNumbers: false,
                                theme: 'material',
                                mode: 'go',
                            }}
                        />
                    </div>
                </div>
            </div>
        </Form>
    );
}

export default Editor;