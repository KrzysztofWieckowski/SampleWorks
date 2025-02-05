/// <reference types="cypress" />

declare namespace Cypress {
  interface Chainable<Subject = any> {
    selectOnCalendar(): Chainable<any>;
    goodBooking(): Chainable<any>;
  }
}
