/* TESTS:
1. Verify expected entities
2. Add, save entity and verify its presence
3. Activate and verify matching
4. Verify Entity filter
*/

import {ENTITIES, PAGES} from "../../support/enums";

describe('RECRUITMENT TASKS', () => {
    beforeEach(() => {
        cy.visit(PAGES.MATCHING);
    });

    it('1. Verify expected entities', () => {
        cy.verifyEntityNames();
    });

    it('2. Add, save entity and verify its presence', () => {
        cy.verifyEntityName(ENTITIES.NEW_ENTITY);
    });

    it('3. Activate and verify matching', () => {
        cy.verifyMatching();
    });

    it('4. Verify Entity filter', () => {
        cy.verifyEntityFilter()
    });
});
