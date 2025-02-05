export const expectedEntities = (): string[] => [
    "Maching LLC",
    "Alpha Investments",
    "Beta Holdings",
    "Gamma Ventures",
    "Delta Capital",
    "Epsilon Funds"
];

export const validateChanges = (arr1: string[], arr2: string[]): any => {
    expect(arr1.length).to.equal(arr2.length); // Ensure arrays are the same length

    arr1.forEach((status, index) => {
        if (status === "Approved") {
            expect(arr2[index]).to.equal("Closing", `Index ${index} should be Closing`);
        } else if (status === "Pending") {
            expect(arr2[index]).to.equal("Approved", `Index ${index} should be Approved`);
        } else {
            throw new Error(`Unexpected status: ${status} at index ${index}`);
        }
    });
};

export const sortAscending = (array): string[] => array.sort((a, b) => a - b)
