import { ChakraProvider, extendTheme } from "@chakra-ui/react";
import { Translator } from "./components/Translator";

const theme = extendTheme({});

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Translator />
    </ChakraProvider>
  );
}

export default App;