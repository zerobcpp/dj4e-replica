import React, {useState, useEffect} from 'react'
import getProducts from "./helper/Calls.js"

function Home() {
  const [products, setProducts] = useState([]);
  const [errors, setErrors] = useState(false);
  
  const loadProducts = () => {
    getProducts()
    .then(data => {
      if (data.error){
        setErrors(data.error);
        console.log(error);
      }
      else{
        setProducts(data);
      }
    })
    .catch(err => console.log(err));
  };

  useEffect(()=>{
    loadProducts();
  }, [])
  

  return (
    <div>
        <h1>home page</h1>
        <div className="product-row">
          {products.map( (product, idx) => {
            return(
              <div className="product-column" key={idx}>
                <h1>
                  {product.name}
                </h1>
                <br>
                </br>
              </div>
            )
          })
          
          }

        </div>
    </div>
  )
}

export default Home


