

import Editor from './components/Editor';
import Home from './components/Home';
import Symbols from './components/Symbols_Table';
import Errors from './components/Errors';
import Optimize from './components/Optimize_Table';

import Navigation from './components/Navigation';
import { Route, Switch } from 'react-router-dom';

function App() {
  return (
    <div className="App" style={{ width: 100 + "%", height: 100 + "vh" }}>

      <Navigation />
      <Switch>
        <Route exact path='/' component={Home} />
        <Route path='/Bienvenida' component={Home} />

        <Route path='/Editor' component={Editor} />

        {/* <Route path='/Compilar' render={Edito} /> */}
        {/* <Route path='/Mirilla' component={Crosshair} />  */}
        {/* <Route path='/Bloques' component={Blocks} />  */}

        <Route path='/TablaSimbolos' component={Symbols} />
        <Route path='/Errores' component={Errors} />
        {<Route path='/Optimizacion' component={Optimize} />}
      </Switch>


    </div >

  );
}

export default App;
