import axios from 'axios';
// eslint-disable-next-line
import React, { useEffect, useState } from 'react'
import { Table } from 'react-bootstrap';

const Optimize = () => {
    // eslint-disable-next-line
    const [optmizations, updateOptmizations] = useState([]);

    useEffect(() => {
        async function fetch() {
            await axios
                .get("http://localhost:5000/Optimizacion")
                .then(response => {
                    if (response) {
                        
                        let a=response.data.optimize
                        for (let index = 0; index < a.length; index++) {
                            if (a[index-1]!='"'){

                            
                            let vari=a[index].split(",")
                            let vari2={
                                "Tipo":"Mirilla",
                                "Regla":vari[0],
                                "Antes":vari[1],
                                "Despues":vari[2],
                                "Linea":vari[3]

                            }
                            updateOptmizations(optmizations=>[...optmizations,vari2])
                        }
                        }
                        console.log(optmizations)
                    }
                })
        }
        console.log(optmizations)
        fetch()
    }, [])

    return (
        <div className="container " style={{width: 100 + "%", height: 88.2 + "vh" }}>
			   <h1 style={{ color: "white" }}>Tabla de optimizaciones</h1>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>Regla</th>
                        <th>Antes</th>
                        <th>Despues</th>
                        <th>Linea</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        optmizations ? optmizations.map(item => {
                            return (
                                <tr key={item}>
    
                                    <td>{item.Regla}</td>
                                    <td>{item.Antes}</td>
                                    <td>{item.Despues}</td>
                                    <td>{item.Linea}</td>
                                </tr>
                            );
                        }): null
                    }
                   
                </tbody>
            </Table>
        </div>
    );
}

export default Optimize;