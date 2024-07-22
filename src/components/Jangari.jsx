import { useEffect, useState } from "react";
import heroBg from "../assets/heroBg.png"
import { Link } from "react-router-dom";
const Jangari = () => {
  const [jangari,setJangari] = useState([])
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/rest/jangari/');
        const data = await response.json();
        setJangari(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  console.log(jangari);
    return (
      <section  className=' min-h-screen absolute top-0 left-0 w-full'  style={{ backgroundImage: `url(${heroBg})` }}>
         <div className=" container mx-auto px-4">
              <div className=" mt-[180px]  grid  grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">

                  {
                    jangari.length > 0 && jangari.map((item)=>{

                     return <div className="  bg-slate-800 rounded-xl  border border-white" key={item.id}>
                        <Link to={`/jangari/${item.id}`}>
                          <img  className=" cursor-pointer w-full  h-[150px]  object-cover  rounded-t-xl mb-2" src={item.photo} alt="l" />
                        </Link>
                          <h3 className=" p-2 text-gray-400 text-[14px]">{item.title}</h3>
                         </div>

                    })
                  }

              </div>
         </div>
      </section>
    );
  };
  
  export default Jangari;
  