import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'http://localhost:5173', //endereço do front
  },
  //tamanho tela
  viewportHeight: 950,
  viewportWidth: 1300,
});
