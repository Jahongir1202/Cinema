import  { useEffect } from 'react'
import { useParams } from 'react-router-dom';

const CinimaId = () => {
    const {id }= useParams()
    console.log(id);
    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch(`http://127.0.0.1:8000/rest/cinema/${id}`);    
            const data = await response.json();
            // setJangari(data);
            console.log(data);
          } catch (error) {
            console.error("Error fetching data:", error);
          }
        };
        fetchData();
      }, []);
  return (
    <section>
        cinema
    </section>
  )
}

export default CinimaId
