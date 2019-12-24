// Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function arrNum(){
    var arr=[];
    for(var i=1; i<256; i++)
        arr.push(i);
    return arr;
}   
console.log(arrNum())

// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
function sumEven(){
    var sum=0;
    for( var i=2; i<1001; i+=2)
        sum+=i;
    return sum;
}
console.log(sumEven());

// Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
function sumOdd(){
    var sum=0;
    for( var i=1; i<=5000; i+=2)
        sum+=i;
    return sum;
}
console.log(sumOdd());

// Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function SumArray(arr){
    var sum=0;
    for(var i=0; i<arr.length-1;i++){
        sum+=arr[i];
    }  
    return sum;
}
console.log(SumArray([1,5,3,-8]));

// Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

function maxNum(arr){
    max=0
    for( var i=0; i<arr.length; i++){
        if( arr[i] >max){
            max=arr[i];
        }
    } 
    return max;
}
console.log(maxNum([3,-3,5,6,1]))

// Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
function average(){
    sum=0
    for (var i=0; i<arr.length;i++){
        sum+=arr[i];
    }
    return sum/arr.length
}   

// Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
function oddNUm(){
    var arr=[]
    i=1;
    while (i <=50){
        arr.push(i);
        i+=2;    
    }
    return arr
}
console.log(oddNUm())

// Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater
//  than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
function greaterthanY(arr,Y){
    var count=0;
    for(var i=0; i<arr.length; i++){
        if (arr[i]>Y){
            count++;
        }
    }
    return count;
}




