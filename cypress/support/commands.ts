import {CHECKBOXES, ENTITIES, LOCATOR, PAGES} from "./enums";
import {expectedEntities, sortAscending, validateChanges} from "./helpers";

Cypress.Commands.add("getByDC", (dataCy) => {
    cy.get(`[data-cy='${dataCy}']`);
});

Cypress.Commands.add("clickByDC", (dataCy) => {
    cy.getByDC(dataCy).click();
});

Cypress.Commands.add("verifyEntityNames", () => {
    // arrange
    let allEntities: string[] = [];

    // act
    cy.getByDC(LOCATOR.ENTITY).each((element) => {
        allEntities.push(element.text());
    }).then(() => {

        // assert
        expect(allEntities.length).to.eq(expectedEntities().length);
        expectedEntities().forEach((expectedEntity) => {
            expect(allEntities).to.include(expectedEntity);
        });
    });
});

Cypress.Commands.add("addNewInvestor", (newEntity) => {
    // arrange

    /* ADDING NEW INVESTOR

    cy.clickByDC(LOCATOR.ADD_INVESTOR_BTN)
    cy.clickByDC(LOCATOR.SAVE_INVESTOR_BTN)

    + an assertion that the new investor is added/saved correctly

    */
});

Cypress.Commands.add("verifyEntityName", (expectedEntity) => {
    // arrange
    let entities: string[] = [];

    cy.addNewInvestor(ENTITIES.NEW_ENTITY);

    // act
    cy.getByDC(LOCATOR.ENTITY).each((element) => {
        entities.push(element.text());
    }).then(() => {

        // assert
        expect(entities).to.include(expectedEntity);
    });
});

Cypress.Commands.add("verifyMatching", () => {
    // I assume that the order of entities records does not change after pressing the matching button!!!
    // arrange
    let allStatuses: string[] = [];
    let newStatuses: string[] = [];
    const suggestedEntity = expectedEntities()[0];
    const closingEntity = expectedEntities()[1];

    // act
    cy.getByDC(LOCATOR.STATUS).each((element) => {
        allStatuses.push(element.text());
    }).then(() => {

        /* ACTIVATING MATCHING
        cy.clickByDC(LOCATOR.START_MATCHING_BTN)
        */

        // assert
        // I assume that the order of entities records does not change after pressing the matching button!!!

        // act
        cy.getByDC(LOCATOR.STATUS).each((element) => {
            newStatuses.push(element.text());
        }).then(() => {

            // assert
            validateChanges(allStatuses, newStatuses); // currently FAILS -> static page

            // arrange
            cy.contains(suggestedEntity).click();

            // assert
            cy.getByDC(LOCATOR.SUGGESTED).then((element) => {
                const suggestedElementsTest = element.text();

                // assert
                expect(suggestedElementsTest).to.include(suggestedEntity); // currently FAILS -> static page
            });
            cy.getByDC(LOCATOR.CLOSING).then((element) => {
                const closingElementsTest = element.text();

                // assert
                expect(closingElementsTest).to.include(closingEntity); // currently FAILS -> static page
            });
        });

        // assert
        cy.verifyVisibilityCheckboxes(); // currently FAILS -> static page
    });
});

Cypress.Commands.add("verifyVisibilityCheckboxes", () => {
    // arrange
    let visibilityCheckboxes: string[] = [];

    // act
    cy.getByDC(LOCATOR.VISIBILITY_CHECKBOX).each((element) => {
        visibilityCheckboxes.push(element.text());
    }).then(() => {

        // assert
        expect(visibilityCheckboxes).to.not.include(CHECKBOXES.NOT_CHECKED); // currently FAILS -> static page
    });
});

Cypress.Commands.add("verifyEntityFilter", () => {
    // arrange
    let allEntities: string[] = [];
    let filteredEntities: string[] = [];

    cy.getByDC(LOCATOR.ENTITY).each((element) => {
        allEntities.push(element.text());
    }).then(() => {

        // act
        cy.clickByDC(LOCATOR.FILTER_BTN);
        cy.getByDC(LOCATOR.ENTITY).each((element) => {
            allEntities.push(element.text());
        }).then(() => {

            // assert
            expect(sortAscending(allEntities)).to.eq(filteredEntities); // currently FAILS -> no filtering available
        });
    });
});
