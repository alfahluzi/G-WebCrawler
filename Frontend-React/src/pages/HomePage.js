import React from "react";
import axios from "axios";
class HomePage extends React.Component {
	constructor(props) {
		super(props);
		this.state = { value: "", result: "", inputType: 0 };
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleChange(event) {
		this.setState({ value: event.target.value });
	}

	handleSubmit(event) {
		console.log(this.state.value);
		let url = "";
		if (this.state.inputType == 0)
			url = `http://127.0.0.1:5000/googlecrawl/${this.state.value}`;
		if (this.state.inputType == 1)
			url = `http://127.0.0.1:5000/crawl/${this.state.value}`;

		axios.get(url).then((response) => {
			let res = response.data;
			console.log(res.header);
			console.log(res.link);
			console.log(res.pharagrap);
			this.setState({
				result: {
					header: res.header,
					link: res.link,
					pharagrap: res.pharagrap,
				},
			});
		});
		event.preventDefault();
	}
	render() {
		return (
			<div className="m-5">
				<button
					className={
						"border-1 ring-2 rounded m-2 p-1 " +
						(this.state.inputType === 0 ? "bg-cyan-200" : "")
					}
					onClick={() => {
						this.setState({ inputType: 0 });
					}}
				>
					Google Search
				</button>
				<button
					className={
						"border-1 ring-2 rounded m-2 p-1 " +
						(this.state.inputType === 1 ? "bg-cyan-200" : "")
					}
					onClick={() => {
						this.setState({ inputType: 1 });
					}}
				>
					By URL
				</button>
				<form onSubmit={this.handleSubmit}>
					<div class="sm:col-span-4 ">
						<label
							for="username"
							class="block text-sm font-medium leading-6 text-gray-900"
						>
							Insert Google Keyword or URL
						</label>
						<div class="">
							<div class="flex rounded-md shadow-sm ring-2 ring-inset ring-gray-300 ">
								<input
									type="text"
									class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 "
									value={this.state.value}
									onChange={this.handleChange}
								/>
							</div>
						</div>
						<input
							type="submit"
							className="border-1 ring-2 rounded m-1 px-1 "
							value="Submit"
						/>
					</div>
				</form>
				<div className="mt-6">
					<label
						for="username"
						class="block text-sm font-medium leading-6 text-gray-900"
					>
						Result
					</label>
					<div class="flex rounded-md shadow-sm ring-2 ring-inset ring-gray-300">
						<div class="block w-full min-h-[50px] border-0 bg-transparent py-1.5 pl-1 text-gray-900">
							{this.state.result.link}
						</div>
					</div>
					<div class="flex rounded-md shadow-sm ring-2 ring-inset ring-gray-300">
						<div class="block w-full min-h-[50px] border-0 bg-transparent py-1.5 pl-1 text-gray-900">
							{this.state.result.header}
						</div>
					</div>
					<div class="flex rounded-md shadow-sm ring-2 ring-inset ring-gray-300">
						<div class="block w-full min-h-[50px] border-0 bg-transparent py-1.5 pl-1 text-gray-900">
							{this.state.result.pharagrap}
						</div>
					</div>
				</div>
			</div>
		);
	}
}
export default HomePage;
