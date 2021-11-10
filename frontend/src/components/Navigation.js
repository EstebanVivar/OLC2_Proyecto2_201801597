import React from 'react';
import { BiBarChartSquare, BiCodeAlt, BiAnalyse,  BiCodeBlock, BiCrosshair, BiError,  BiGridAlt, BiTable, BiTrendingUp } from 'react-icons/bi';



import { Navbar, Nav, NavDropdown } from 'react-bootstrap';

const Navigation = () => {
  
	let theme="dark";
    return (
        <Navbar className="mb-2" collapseOnSelect  expand="sm" sticky="top" bg={theme} variant={theme} >

            <Navbar.Brand style={{ fontSize: "28px", fontWeight: "bolder" }} href="/Bienvenida">
                &nbsp;&nbsp;&nbsp;JOLC

            </Navbar.Brand>
            <Navbar.Toggle/>
            <Navbar.Collapse  >
                <Nav >
                
                    <Nav.Link  href="/Editor"> &nbsp; <BiCodeAlt size="24px"/> Editor &nbsp;</Nav.Link>


                    <NavDropdown title={<>&nbsp; <BiAnalyse size="24px"/> Compilador</>} id="basic-nav-dropdown">
                        <NavDropdown.Item  href="/Compilar" ><BiCodeBlock/> Compilar</NavDropdown.Item>
                        <NavDropdown.Item  href="/Mirilla"><BiCrosshair/> Optimizar por mirilla</NavDropdown.Item>
                        <NavDropdown.Item  href="/Bloques"><BiGridAlt/> Optimizar por bloques</NavDropdown.Item>
                    </NavDropdown>

                    <NavDropdown title={<>&nbsp; <BiBarChartSquare size="24px" /> Reportes</>} id="basic-nav-dropdown">
                        <NavDropdown.Item  href="/TablaSimbolos"> <BiTable/> Tabla de simbolos</NavDropdown.Item>                        
                        <NavDropdown.Item  href="/Errores"><BiError/> Errores</NavDropdown.Item>
                        <NavDropdown.Item  href="/Optimizacion"><BiTrendingUp/> Optimizacion</NavDropdown.Item>
                    </NavDropdown>
                </Nav>

            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation;