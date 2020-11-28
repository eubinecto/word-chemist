import './App.css';
import React, { Component } from 'react'
import Select from 'react-select'
import axios from 'axios'
import { Fireworks } from 'fireworks/lib/react'

export default class App extends Component {

  constructor(props){
    super(props)
    this.state = {
      selectOptions : [],
      id: "",
      name: '',
      type: "nothing",
      current: "Something",
      target:  "Something",
      gameState: 0
    }
  }

 async getOptions(){
    const res = await axios.get('https://jsonplaceholder.typicode.com/users')
    const data = res.data

    const options = data.map(d => ({
      "value" : d.id,
      "label" : d.name
    }))

    this.setState({selectOptions: options})

  }

  handleChange(e){
   this.setState({id:e.value, name:e.label})
  }

  handleSubmit = event => {
    event.preventDefault();

    const user = {
      name: this.state.name
    };

    if (this.state.type==="add"){
      console.log("Adding");
      axios.post(`https://jsonplaceholder.typicode.com/users`, { user })
        .then(res => {
          console.log(res);
          console.log(res.data);
        })
    } else if (this.state.type==="sub"){
      console.log("Substracting");
      axios.post(`https://jsonplaceholder.typicode.com/users`, { user })
        .then(res => {
          console.log(res);
          console.log(res.data);
        })
    }
  }

  componentDidMount(){
      this.getOptions()
  }

  handleClick = event => {
    this.setState({type:event.target.id});
  }
  game(props){
    if (props.gameHasStarted){
      
    } else{

    }
  }
  beginGame = event =>{
    this.setState({gameState: 1});
  }
  winGame = event =>{
    this.setState({gameState: 2});
  }
  endGame = event =>{
    this.setState({gameState: 0});
  }
  

  render() {
    console.log(this.state.gameState)
    if (this.state.gameState === 1){
      return (
        <div id = "Option">
          <h1>Your current is: {this.state.current} Your target is: {this.state.target}</h1>
          <Select options={this.state.selectOptions} onChange={this.handleChange.bind(this)} />
            <p>You have selected <strong>{this.state.name}</strong> whose id is <strong>{this.state.id}</strong></p>
          <form onSubmit={this.handleSubmit}>
            <button id="add" type="submit" onClick={this.handleClick.bind(this)}>Add</button>
            <button id="sub" type="submit" onClick={this.handleClick.bind(this)}>Substract</button>
          </form>
          <form onSubmit={this.winGame}>
            <button id="begin" type="submit">Win Game</button>
          </form>   
        </div>
      );
    }
    else if (this.state.gameState === 0) {
      return(
        <div>
          <h1>Click the button to begin the game</h1>
          <form onSubmit={this.beginGame}>
            <button id="begin" type="submit">Begin Game</button>
          </form>
        </div>
        );
    }
    else if (this.state.gameState === 2){
      let fxProps = {
        count: 3,
        interval: 200,
        colors: ['#cc3333', '#4CAF50', '#81C784'],
        calc: (props, i) => ({
          ...props,
          x: (i + 1) * (window.innerWidth / 3) - (i + 1) * 100,
          y: 200 + Math.random() * 100 - 50 + (i === 2 ? -80 : 0)
        })
      }
      return (
        <div>
          <Fireworks {...fxProps} />
          <h1>Congrats!</h1>
          <form onSubmit={this.beginGame}>
            <button id="begin" type="submit">Play again</button>
          </form>
        </div>
      )
    }
  }
}