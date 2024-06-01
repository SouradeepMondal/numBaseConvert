// Example: GET request
async function userAction (number, inputBase, outputBase) {
  const response = await fetch('http://localhost:5000/api/v1.0/numBaseConvert?number=10&inputBase=10&outputBase=10')
  const data = await response.json()
  var output = document.getElementById('outputNumber');
  output.innerHTML = data['Output Number']
  console.log(data)
        
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
