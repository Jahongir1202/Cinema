import heroBg from "../assets/hero-min.jpg";
import Movi from "./Movi";

const Home = () => {
  return (
    <>
    <header style={{ backgroundImage: `url(${heroBg})` }} className="   w-full h-screen">
       
      <div
        className="default-ltr-cache-1y1tnl9 egicmjq0"
        style={{
          backgroundImage: "linear-gradient(to top, rgba(0, 0, 0 ,0.8) 0%, rgba(0, 0, 0, 0) 60%, rgba(0, 0, 0,0.2) 100%)",
        }}
        data-uia="nmhp-card-hero+gradient"
      ></div>
  
    </header>
   <Movi/>

    </>
  );
};

export default Home;