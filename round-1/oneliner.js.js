const solvehacky = (str1,str2)=>str1.split('').map((c,i)=>c+(str2[i]||'')).join('')+str2.slice(str1.length);
console.time ('perf');
for (var i=10000000; i--;) {
   let str1 = 'abacate' + i
   let str2 = 'palmeiras' + i
   let result = solvehacky(str1,str2)
 }
console.timeEnd ('perf');