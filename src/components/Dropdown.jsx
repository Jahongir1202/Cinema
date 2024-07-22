import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import dropdown from "../assets/dropdown-arrow-svgrepo-com.svg";

const Dropdown = ({ title, isOpen, setIsOpen }) => {
  const [janr, setJanr] = useState([]);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/rest/jangari/');
        const data = await response.json();
        setJanr(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="relative z-10 w-full">
      <button onClick={toggleDropdown} className="w-full flex items-center gap-2 text-white text-[20px] hover:text-stone-300 md:text-gray-300 tracking-widest md:hover:text-gray-200">
        <span>{title}</span>
        <img src={dropdown} alt="dropdown" className="pt-1.5" />
      </button>
      {isOpen && (
        <ul className="absolute left-0 mt-2 bg-transparent backdrop-blur-sm md:w-44 w-full bg-slate-900 border border-white rounded-lg shadow-lg z-10">
        
            <li>
              <Link to={'/jangari'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Jangari
              </Link>
            </li>
            <li>
              <Link to={'/'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Komedia
              </Link>
            </li>   <li>
              <Link to={'/'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Drama
              </Link>
            </li>   <li>
              <Link to={'/'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Ujas
              </Link>
            </li>   <li>
              <Link to={'/'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Romance
              </Link>
            </li>   <li>
              <Link to={'/'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Fantastik
              </Link>
            </li>
            <li>
              <Link to={'/'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Hayotiy
              </Link>
            </li>
        </ul>
      )}
    </div>
  );
};

export default Dropdown;
