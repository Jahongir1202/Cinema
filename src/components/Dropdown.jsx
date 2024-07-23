
import { Link } from "react-router-dom";
import dropdown from "../assets/dropdown-arrow-svgrepo-com.svg";

const Dropdown = ({ title, isOpen, setIsOpen }) => {

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  
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
              <Link to={'/comedia'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Komedia
              </Link>
            </li>   <li>
              <Link to={'/drama'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Drama
              </Link>
            </li>   <li>
              <Link to={'/ujas'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Ujas
              </Link>
            </li>   <li>
              <Link to={'/romance'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Romance
              </Link>
            </li>   <li>
              <Link to={'/fantastik'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Fantastik
              </Link>
            </li>
            <li>
              <Link to={'/hayotiy'} className="block px-4 py-2 text-white border-b border-transparent hover:border-white rounded-2xl" onClick={() => setIsOpen(false)}>
               Hayotiy
              </Link>
            </li>
        </ul>
      )}
    </div>
  );
};

export default Dropdown;
