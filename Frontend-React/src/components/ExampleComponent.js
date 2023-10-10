import React from "react";

class ExampleComponent extends React.Component {
	render() {
		return (
			<div className="w-screen h-[50px] shadow-lg fixed bg-slate-100">
				<div className="flex flex-row justify-center mt-2 lg:justify-end lg:mr-64 text-slate-600 space-x-10 text-lg font-bold">
					Header
				</div>
			</div>
		);
	}
}
export default ExampleComponent;
