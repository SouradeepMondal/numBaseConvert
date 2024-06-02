// Example: GET request
async function userAction (number, inputBase, outputBase) {
  const baseUrl = "http://localhost:5000/api/v1.0/numBaseConvert?";
  const finalUrl = `${baseUrl}number=${number}&inputBase=${inputBase}&outputBase=${outputBase}`;
  const response = await fetch(finalUrl)
  const data = await response.json()
  var output = document.getElementById('outputNumber');
  output.innerHTML = data['Output Number']
  // console.log(data)
        
};

// // Example: POST request
// const postData = { key1: 'value1', key2: 'value2' };
// const postAction = async () => {
//     try {
//         const response = await fetch('https://api.example.com/data', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(postData)
//         });
//         const data = await response.json();
//         // Handle the response data here
//     } catch (error) {
//         console.error('Error posting data:', error);
//     }
// };
