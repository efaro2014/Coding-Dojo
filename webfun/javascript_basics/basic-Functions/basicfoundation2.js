// Create a function that takes in an array of numbers.  The function 
// should print the lowest value in the array, and return the highest value in the array
+
function lowestandhighest(arr){
    var max=0
    var min =0 
    for(i=0; i<arr.length; i++){
        if (arr[i]> max){
            max=arr[i];
            
        }
        else if (arr[i]<min){
            min=arr[i];
        }
    }
    console.log(min)
    return max;
}
var arr=[1,3,25,-1,6]
lowestandhighest(arr)


// Build a function that takes in an array of numbers.  The function should print the second-to-last value in the array,
//  and return the first odd value in the array.

function firstOdd(arr){
    var newarr=[]
    for(var i =0; i<arr.length;i++){
        if(i%2!=0){
            newarr.push(i);
        }
    }
    console.log(arr.slice(1,arr.length));
    return newarr[0];
}
firstOdd([1,3,2,5,4,7]);
// console.log(firstOdd([1,3,2,5,4,7]));

// create a function that returns a new array where each value in the original array has been doubled.  
// Calling double([1,2,3]) should return [2,4,6] without changing the original array.
function doubleVision(arr){
    for(var i=0; i<arr.length;i++){
        arr[i]= arr[i]*2
    }
    return arr
}
console.log(doubleVision([1,2,3]))

// Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.  
// Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.
function countPositives(arr){
    count = 0
    for(var i=0; i<arr.length;i++){
        if (arr[i]>0){
            count+=1;
        }
    }
    arr[arr.length]=count
    return arr
}
console.log(countPositives([-1,2,1,2-1]))

// Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".  Every time the array 
// has three evens in a row, print "Even more so!".
function oddEven(arr){
    for (var i=0; i<arr.length;i++){
        if(arr[i]%2!=0 && arr.slice(i,i+3 )){
        }
            console.log('Odd');
    }    
}
oddEven([1,2,1,3,2,1])


// Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], 
    // arr[3], arr[5], etc).  Afterward, console.log each array value and return arr.

function oddIndex(arr){
    for(var i=0; i<arr.length; i++){
        if (i%2!=0){
            arr[i]=arr[i]+1;
        }
    }
    return arr;
}
console.log(oddIndex([1,1,1,1,1]));

