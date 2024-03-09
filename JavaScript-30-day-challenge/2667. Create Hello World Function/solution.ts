function createHelloWorld() {
    
    return function(...args): string {
        return ((): string => {return "Hello World";})()
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
