import { Component } from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";

class App extends Component {
	render() {
		return (
			<div>
				<div>
					<Routes>
						<Route path="/" element={<HomePage />} />
					</Routes>
				</div>
			</div>
		);
	}
}

export default App;
