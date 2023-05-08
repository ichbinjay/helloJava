/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let original = init;
    let increment = ()=>{ init+=1; return init; }
    let decrement = ()=>{init-=1; return init; }
    let reset = ()=>{init=original; return init; }

    return {increment, decrement,reset }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
