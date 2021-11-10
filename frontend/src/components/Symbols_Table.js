// import axios from 'axios'
// eslint-disable-next-line
import React, { useEffect, useState } from 'react'
import { Table } from 'react-bootstrap';

const Symbols = () => {
    // eslint-disable-next-line
    const [simbols, updateSimbols] = useState([]);

    // useEffect(() => {
        // async function fetch() {
        //     await axios
        //         .post("https://quiet-springs-28392.herokuapp.com/TablaSimbolos")
        //         .then(response => {
        //             if (response) {
        //                 updateSimbols(response.data)
        //             }
        //         })
        // }
        // fetch()
    // }, [])

    return (
        <div className="container " style={{width: 100 + "%", height: 88.2 + "vh" }}>
        <h1 style={{ color: "white" }}>Tabla de simbolos</h1>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Entorno</th>
                        <th>Tipo</th>
                        <th>Fila</th>
                        <th>Columna</th>
                    </tr>
                </thead>
                <tbody>                   
                    {simbols.map(item => {
                        return (
                            <tr key={item.id}>

                                <td>{item.id}</td>
                                <td>{item.ambito}</td>
                                <td>{item.tipo}</td>
                                <td>{item.fila}</td>
                                <td>{item.columna}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </Table>
        </div>
    );
}

export default Symbols;