import { Link } from "react-router-dom";

const Cart = ({ id, src, titile, category, type }) => {
  return (
    <div className=" flex flex-col  gap-2 text-gray-300 rounded-t-xl">
      <Link to={type === 'cinema' ? `/cinema/${id}` : type === "multifilm" ? `/multifilm/${id}` : `/serial/${id}`}>
        <img src={src} alt={titile}  className=" rounded-t-xl w-[180px] h-[220px] object-cover"/>
      </Link>
      <h3 className=" text-[16px]  tracking-widest">{titile}</h3>
    </div>
  );
};

export default Cart;
