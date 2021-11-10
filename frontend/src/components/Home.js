import React from "react";
import image from "../home.png"
const Home = () => {

	let font_color = "white"
	return (
		<div className="container-fluid mb-5">
			<div className="row" style={{
				minHeight: " 100%",
				display: "flex",
				alignItems: "center"
			}}>
				<div className="col-md-6  mt-2 d-flex justify-content-center" style={{ float: "none", margin: "auto" }}>
					<img src={image} style={{ maxWidth: "380px", width: 70 + "%", height: 70 + "%" }} alt="load" />
				</div>

				<div className="col-md-6  mt-4 " >
					<h2 className="display-2" style={{ fontFamily: 'Roboto Condensed', color: `${font_color}` }}>
						Hola, soy Carlos Vivar
					</h2>
					<h2 className="display-4 " style={{ fontFamily: 'Roboto Condensed', color: `${font_color}` }}>
						201801597
					</h2>

					<h4 style={{ alignContent: "center", fontFamily: 'Roboto Condensed', color: `${font_color}` }}>
						OLC2 B <br />
						Ingenieria de Ciencias y Sistemas <br />
						Universidad San Carlos de Guatemala
					</h4>
				</div>
			</div>
		</div>
	);
}

export default Home;

