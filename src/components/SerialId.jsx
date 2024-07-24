import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Detail from './Detail';

const SerialId = () => {
  const [data, setData] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/rest/serial/${id}`);
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
  }, [id]);

  return (
    <section>
      {data ? (
        <Detail 
          title={data.movia?.title} 
          genre={data.movia?.genre} 
          country={data.movia?.state} 
          year={data.movia?.years} 
          watch={data.movia?.views_count}
          name={data.movia?.subtitle}
          imageUrl={data.movia?.photo}
          videoUrl={data.videos}
        />
      ) : (
        <p className='text-center font-semibold text-[24px]'>Yuklanmoqda...</p>
      )}
    </section>
  );
}

export default SerialId;
