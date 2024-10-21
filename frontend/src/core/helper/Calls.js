
const getProducts = () => {
    let API = process.env.API
    console.log(`${API}/product/`)
    return (
    fetch(`${API}/product/`, {method:'GET'})
    .then(res => {
        return res.json();
    })
    .catch(e => console.log(e))
)};

export default getProducts