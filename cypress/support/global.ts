import { LOCATOR } from './enums';

declare global {
    namespace Cypress {
        interface Chainable {
            /**
             * Verifies entity names and amount of entities
             */
            verifyEntityNames(): void;

            /**
             * Gets element by data-cy attribute
             */
            getByDC(dataCy: string): Chainable<JQuery<HTMLElement>>;

            /**
             * Click element by data-cy attribute
             */
            clickByDC(dataCy: string): Chainable<JQuery<HTMLElement>>;

            /**
             * Adds new investor
             */
            addNewInvestor(newEntity: string): void;

            /**
             * Verifies expected entity name
             */
            verifyEntityName(expectedEntity: string): void;

            /**
             * Verifies matching
             */
            verifyMatching(): void;

            /**
             * Verifies that all visibility checkboxes are checked
             */
            verifyVisibilityCheckboxes(): void;

            /**
             * Verifies changes on the investor account page
             */
            verifyInvestorAccount(): void;

            /**
             * Verifies entity filter
             */
            verifyEntityFilter(): void;
        }
    }
}
