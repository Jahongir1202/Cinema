import heroBg from "../assets/hero-min.jpg";
import Movies from "./Movies";

const Home = () => {
  return (
    <>
    <header style={{ backgroundImage: `url(${heroBg})` }} className=" absolute top-0 left-0 w-full h-screen">
      <div
        className="default-ltr-cache-1y1tnl9 egicmjq0"
        style={{
          backgroundImage: "linear-gradient(to top, rgba(0, 0, 0 ,0.8) 0%, rgba(0, 0, 0, 0) 60%, rgba(0, 0, 0,0.2) 100%)",
        }}
        data-uia="nmhp-card-hero+gradient"
      ></div>
    </header>
    <Movies/>
    </>
  );
};

export default Home;