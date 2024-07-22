import { Link } from "react-router-dom";

const Cart = ({ id, src, titile, category, link }) => {
  return (
    <div>
      <Link to={link} >
        <img src={src} alt={titile} />
      </Link>
      <h3>{titile}</h3>
    </div>
  );
};

export default Cart;
