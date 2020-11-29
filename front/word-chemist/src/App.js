import './App.css';
import React, { Component } from 'react'
import Select from 'react-select'
import axios from 'axios'
import { Fireworks } from 'fireworks/lib/react'

export default class App extends Component {

  constructor(props){
    super(props)
    this.state = {
      result: 0,
      selectOptions : [],
      resOptions : [],
      id: "",
      name: '',
      type: "nothing",
      current: "Something",
      target:  "Something",
      gameState: 0,
      moves: 2,
      selLabel: ""  
    }
  }

  async getSrcDest(){
    console.log("making request")
    const res = await axios.get('http://125.181.29.86:5000/word_chemist/src_dest')
    const data = res.data
    this.setState({
      current: data[0],
      target: data[1]
    })
  }

 async getOptions(){
    const res = await axios.get('http://125.181.29.86:5000/word_chemist/all_choices')
    const data = res.data

    const options = data.map(d => ({
      "value" : d,
      "label" : d
    }))

    this.setState({selectOptions: options})
  }

  handleChange(e){
   this.setState({id:e.value, name:e.label})
  }

  handleState (e){
    this.setState({selLabel: e.label});
  }


  handleSubmit = event => {
    event.preventDefault();

    const user = {
      name: this.state.name
    };
    if (this.state.type==="add"){
      console.log("adding");
      axios.get(`http://125.181.29.86:5000/word_chemist/add_or_sub`,{ 
        params: {
        op: "add",
        first: this.state.current,
        second: this.state.name,
        topn: 1
      }
    }).then((response) => {
        const data = response.data;
        const options = data.map(d => ({
          "value" : d[1],
          "label" : d[0]
        }));
        this.setState({resOptions:options});
      }, (error) => {
        console.log(error);
    });
    } else if (this.state.type==="sub"){
        const res = axios.get(`http://125.181.29.86:5000/word_chemist/add_or_sub`,{ 
        params: {
        op: "sub",
        first: this.state.current,
        second: this.state.name,
        topn: 1
      }
    }).then((response) => {
      const data = response.data;
      const options = data.map(d => ({
        "value" : d[1],
        "label" : d[0]
      }));
      this.setState({resOptions:options});
    }, (error) => {
      console.log(error);
  });
    
    }
    // if (this.state.current===this.state.target){
    //   this.winGame();
    // }
  }

  componentDidMount(){
      this.getOptions()
  }

  handleClick = event => {
    this.setState({type:event.target.id});
  }
  
  beginGame = event =>{
    this.setState({gameState: 1});
    this.setState({moves: 2});
    this.setState({result: 0});
    this.getSrcDest();
    this.updateScore();
  }
  calculateScore(){
    const res = axios.get(`http://125.181.29.86:5000/word_chemist/cos_dist`,{ 
        params: {
        first: this.state.current,
        second: this.state.target,
      }
    }).then((response) => {
      const data = response.data;
      console.log(data);
      var score = data;
      this.setState({result:score}, () =>{
        console.log("This highscore: " + this.state.result);
        this.winGame();
      });
    }, (error) => {
      console.log(error);
  });
  }

  updateScore(){
    const res = axios.get(`http://125.181.29.86:5000/word_chemist/cos_dist`,{ 
        params: {
        first: this.state.current,
        second: this.state.target,
      }
    }).then((response) => {
      const data = response.data;
      console.log(data);
      var score = data;
      this.setState({result:score});
    }, (error) => {
      console.log(error);
  });
  }

  winGame (){
    console.log("winning game");
    this.setState({gameState: 2});
  }
  endGame = event =>{
    this.setState({gameState: 0});
  }
  
  handleCurrent (event){
    var label = this.state.selLabel;
    this.setState({current: label});
    this.updateScore();
    this.setState({moves: this.state.moves-1}, () => {
      if (this.state.moves===0){
        this.calculateScore();
      }
    });
    
  }

  render() {
    if (this.state.gameState === 1){
      return (
        <div id = "Option">
          <h3>Moves remaining: {this.state.moves}</h3>
          <h1>Your current is: {this.state.current} Your target is: {this.state.target} Your current score: {this.state.result}</h1>
          <Select options={this.state.selectOptions} onChange={this.handleChange.bind(this)} />
            <p>You have selected <strong>{this.state.name}</strong> whose id is <strong>{this.state.id}</strong></p>
          <form onSubmit={this.handleSubmit}>
            <button id="add" type="submit" onClick={this.handleClick.bind(this)}>Add</button>
            <button id="sub" type="submit" onClick={this.handleClick.bind(this)}>Substract</button>
          </form>
          <button id="begin" type="submit" onClick={this.calculateScore.bind(this)}>Win Game</button>
          <h2>Choose appropriate result for your operation</h2>
          <Select options={this.state.resOptions} onChange={this.handleState.bind(this)}/>
          <button id="begin" type="submit" onClick={this.handleCurrent.bind(this)}>Confirm choice</button>
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
      console.log("Score: " + this.state.result);
      return (
        <div>
          <Fireworks {...fxProps} />
      <h1>Congrats! Your score is {this.state.result}</h1>
          <form onSubmit={this.beginGame}>
            <button id="begin" type="submit">Play again</button>
          </form>
        </div>
      )
    }
  }
}