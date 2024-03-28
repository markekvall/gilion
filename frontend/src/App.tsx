// src/App.tsx
import React from 'react';
import AppAppBar from './components/AppAppBar';
import CssBaseline from "@mui/material/CssBaseline"
import {createTheme, ThemeProvider} from "@mui/material/styles";
import Home from './components/Home';
import {PaletteMode} from "@mui/material"


function App() {
  const [mode, setMode] = React.useState<PaletteMode>('dark');
  const defaultTheme = createTheme({palette: {mode}});

  const toggleColorMode = () => {
    setMode((prev) => (prev === 'dark' ? 'light' : 'dark'))
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <CssBaseline/>
      <AppAppBar mode={mode} toggleColorMode={toggleColorMode}/>
        <Home/>
    </ThemeProvider>
  );
}

export default App;
