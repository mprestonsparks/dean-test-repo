// JavaScript code with various issues for agent optimization testing

// Missing strict mode and poor variable declarations
var globalVar = "This should be const/let";

function inefficientArrayOperations(largeArray) {
    // Inefficient array operations
    var result = [];
    for (var i = 0; i < largeArray.length; i++) {
        if (largeArray[i] % 2 === 0) {
            result.push(largeArray[i] * 2);
        }
    }
    return result;
}

// Memory leak - event listeners not cleaned up
function createMemoryLeak() {
    var element = document.createElement('div');
    
    function handleClick() {
        console.log('Clicked');
    }
    
    element.addEventListener('click', handleClick);
    // Missing removeEventListener - causes memory leak
    
    return element;
}

// Callback hell instead of promises/async-await
function nestedCallbacks(callback) {
    setTimeout(function() {
        console.log("First operation");
        setTimeout(function() {
            console.log("Second operation");
            setTimeout(function() {
                console.log("Third operation");
                callback("Done");
            }, 1000);
        }, 1000);
    }, 1000);
}

// Inefficient DOM manipulation
function badDOMManipulation() {
    // Multiple DOM queries for same element
    document.getElementById('myElement').style.color = 'red';
    document.getElementById('myElement').style.fontSize = '16px';
    document.getElementById('myElement').innerHTML = 'Updated';
    
    // Creating elements in loop without fragment
    for (var i = 0; i < 100; i++) {
        var li = document.createElement('li');
        li.textContent = 'Item ' + i;
        document.getElementById('list').appendChild(li);
    }
}

// Poor error handling
function riskyOperation(data) {
    try {
        return JSON.parse(data).value.property.nested;
    } catch (e) {
        console.log("Error occurred");
        // Swallowing errors without proper handling
    }
}

// Inefficient object operations
function inefficientObjectHandling(objects) {
    var result = {};
    
    // Inefficient property copying
    for (var i = 0; i < objects.length; i++) {
        for (var key in objects[i]) {
            result[key] = objects[i][key];
        }
    }
    
    return result;
}

// Missing input validation
function processUserInput(input) {
    // No validation of input
    return eval(input); // Dangerous eval usage
}

// Inefficient string operations
function badStringHandling(strings) {
    var result = "";
    
    // Inefficient string concatenation
    for (var i = 0; i < strings.length; i++) {
        result += strings[i] + ", ";
    }
    
    return result;
}

// Poor async handling
function inefficientAsyncOperations() {
    var promises = [];
    
    // Creating promises in loop without proper batching
    for (var i = 0; i < 10; i++) {
        promises.push(
            fetch('/api/data/' + i)
                .then(response => response.json())
        );
    }
    
    // Not using Promise.all properly
    promises.forEach(promise => {
        promise.then(data => {
            console.log(data);
        });
    });
}

// Missing semicolons and inconsistent formatting
function poorFormatting(  x,y  ){
if(x>y){
return x
}else{
return y
}
}

// Unused variables and functions
function unusedFunction() {
    var unusedVar = "This is never used";
    var anotherUnused = 42;
    
    return "Hello";
}

// Global variable pollution
window.myGlobalData = {
    apiKey: "hardcoded-api-key",
    config: {
        debug: true,
        timeout: 5000
    }
};

// Legacy jQuery-style code
$(document).ready(function() {
    // Old-style event handling
    $('#button').click(function() {
        // Inline event handlers
        $(this).hide();
    });
});

// Export issues (if using modules)
module.exports = {
    inefficientArrayOperations: inefficientArrayOperations,
    nestedCallbacks: nestedCallbacks,
    riskyOperation: riskyOperation
    // Missing other exports
};