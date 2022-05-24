function App(props) {
  return(
    <div>
      <div>hello</div>
      <div>{props.name}</div>
    </div>
  )
}

const root = ReactDOM.createRoot(document.querySelector('#reactApp'));
root.render(<App name="web" />)
