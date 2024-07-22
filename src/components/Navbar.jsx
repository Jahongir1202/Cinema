import React, { useEffect, useState } from "react";
import heroBg from "../assets/hero-min.jpg";
import Logo from "../assets/logo.png";
import { Link } from "react-router-dom";
import Dropdown from "./Dropdown";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

 
  return (
    <nav className="bg-transparent relative z-10">
        <div className="container  mx-auto pr-4 ">
          <div className=" flex flex-wrap items-center justify-between">
            <Link to="/" className=" ">
              <img src={Logo} alt="logo" height={80} width={200} />
            </Link>
            <div className="flex  items-center gap-20">
              <ul className="  hidden md:flex flex-col gap-10 p-4 md:p-0   font-medium bg-transparent  ">
                <li className=" relative">
                  <Dropdown title="Janrlar" isOpen={isOpen} setIsOpen={setIsOpen} />
                </li>
              </ul>

              <div className="relative block">
                <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                  <svg className="w-4 h-4 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                  </svg>
                  <span className="sr-only">Search icon</span>
                </div>
                <input type="text" id="search-navbar" className="block w-full p-2 ps-10 text-sm bg-transparent focus:outline-none outline-none text-white border border-white rounded-lg bg-transparent" placeholder="Search..." />
              </div>
            </div>
          </div>
          <ul className="flex flex-col gap-10 p-4 md:p-0  ml-7  font-medium bg-transparent  md:hidden  w-full">
            <li className=" relative">
              <Dropdown title="Janrlar" isOpen={isOpen} setIsOpen={setIsOpen} />
            </li>
          </ul>
        </div>
      </nav>
  );
};

export default Navbar;
