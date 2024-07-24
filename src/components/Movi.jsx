import React, { useEffect, useState } from 'react'
import Cart from './Cart'
import cinma from "../assets/heroBg.png"
import { Link } from 'react-router-dom'

const Movi = () => {
  const[data,setData]=useState(null)
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/rest/`);
        if (!response.ok) {
          throw new Error('Tarmoq muammosi');
        }
        const data = await response.json();
        setData(data);
      } catch (error) {
        console.error("Ma'lumotni olishda xato:", error);
      }
    };
    fetchData();
  },[]);
  return (
   <section className=' py-[40px] object-cover h-full' style={{ backgroundImage: `url(${cinma})` }} >
    <div className=' container px-4 mx-auto  mb-10'>
          <div className='mb-3 mt-10 flex justify-between items-center'>
          <h2 className=' text-white font-semibold text-[24px] md:text-[44px]'>Kinolar</h2>
          <Link to={'/hamma_kinolar'} className=' text-white'>Hammasi  ko'rish</Link>
          </div>
         
          <div className=' grid grid-cols-2 md:grid-cols-4 gap-6'>
            {
              data?.cinema && data.cinema.map((item)=>{
                return <Cart key={item.id} id={item.id} type={item.type} src={item.photo} titile={item.title}/>
              })
            }
          </div>

          <div className='mb-3 mt-10 flex justify-between items-center'>
          <h2 className=' text-white font-semibold text-[24px] md:text-[44px]'>Serialar</h2>
          <Link to={'/hamma_serialar'} className=' text-white'>Hammasi  ko'rish</Link>
          </div>
          <div className=' grid grid-cols-2 md:grid-cols-4 gap-6'>
            {
              data?.serial && data.serial.map((item)=>{
                return <Cart key={item.id} id={item.id} type={item.type} src={item.photo} titile={item.title}/>
              })
            }
          </div>
          <div className='mb-3 mt-10 flex justify-between  items-center'>
          <h2 className=' text-white font-semibold text-[24px] md:text-[44px]'>Multifilmlar</h2>
          <Link to={'/hamma_multifilmlar'} className=' text-white'>Hammasi  ko'rish</Link>
          </div>
          <div className=' grid grid-cols-2 md:grid-cols-4 gap-6'>
            {
              data?.multifilm && data.multifilm.map((item)=>{
                return <Cart key={item.id} id={item.id} type={item.type} src={item.photo} titile={item.title}/>
              })
            }
          </div>

    </div>
   </section>
  )
}

export default Movi