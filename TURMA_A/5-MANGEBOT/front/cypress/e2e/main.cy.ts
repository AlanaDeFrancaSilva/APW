/// <reference types="cypress" /> // Informa ao editor que estamos usando comandos e tipos do Cypress (para autocomplete e validação)

const el = {
  homePage: ()=> cy.get('#home-page'),
  buildPage: ()=> cy.get('#build-page'),
  cartPage: ()=> cy.get('#cart-page'),
  homeOrderButton: ()=> cy.get('#order'),
  menu: {
    home: ()=> cy.get("#nav-menu #home-menu"),
    cart: ()=> cy.get("#nav-menu #cart-menu"),
    build: ()=> cy.get("#nav-menu #build-menu"),
    translate: ()=> cy.get("#nav-menu #flag"),
  }
}


describe('Home page tests', () => { // Cria um grupo de testes chamado "Home page tests"
  beforeEach(()=>{ //antes de rodar ela sabe que está na home page, portano não precisa repetir o .visit em cada teste
 cy.visit('/')
  })

  it('Check if home page exists', () => {    
    el.homePage().should('exist')
  })

  it('Check if Order Button is Ok', () => {       
    el.homeOrderButton().should('exist')   
    el.homeOrderButton().click()
    el.buildPage().should('exist')
  })
})


//Teste de tradução, mais generico
describe('Translate tests', () => {
  beforeEach(()=>{
    cy.visit('/')
  })

  it('Check if translation feature is Ok', () => {    
    el.menu.home().should('exist')
    el.menu.translate().should('exist')

    el.menu.home().should('contain.text', 'Home')
    el.menu.translate().click()
    el.menu.home().should('contain.text', 'Início')
  })

})


//teste menu
describe('Menu tests', () => {
  beforeEach(()=>{
    cy.visit('/')
    el.homePage().should('exist')
  })

  it('Check if Cart Menu is Ok', () => {
    el.menu.cart().click()
    el.cartPage().should('exist')
  })

  it('Check if Build Menu is Ok', () => { 
    el.menu.build().click()
    el.buildPage().should('exist')
  })

  it('Check if Home Menu is Ok', () => {    
    el.menu.home().click()
    el.homePage().should('exist')
  })

})

//teste Building
describe('Building bots tests', () => {
  beforeEach(()=>{
    cy.visit('/cart')
    el.cartPage().should('exist') 
  }) 

 it('Check if a bot is created', () => {    
    el.cartItem().should('exist') //TERMINAR A LOGICA TEM QUE SER INVERSA, NÃO EXISTIR.
 })

})

