import bgImage from "../assets/heroBg.png";

const Detail = ({ title, genre, country, year, name, imageUrl, videoUrl, watch }) => {
  return (
    <section
      style={{ backgroundImage: `url(${bgImage})` }}
      className="absolute top-0 left-0 w-full min-h-screen bg-cover bg-center"
    >
      <div className="container px-4 mx-auto">
        <div className="mt-[190px] bg-slate-800 flex gap-5 items-start py-5 flex-wrap">
          <div>
            <img
              src={imageUrl}
              alt={title} // Rasm uchun ma'lumot beruvchi alt matn
              className="w-[248px] h-full object-cover"
              loading="lazy"
            />
          </div>
          <div>
            <DetailItem label="Name:" value={title} />
            <DetailItem label="Genre:" value={genre} />
            <DetailItem label="Country:" value={country} />
            <DetailItem label="Year:" value={year} />
            <DetailItem label="Name:" value={name} />
            <DetailItem label="Watch Count:" value={watch} />
          </div>
        </div>

        <div className="mt-20">
          {videoUrl && videoUrl.map((item) => (
            <iframe
            key={item.id}
            src={`http://localhost:8000${item.video_file}`} // Ensure this is correct
            width="100%"
            height="310"
            title={`Video ${item.id}`}
            loading="lazy"
          ></iframe>
          ))}
        </div>
      </div>
    </section>
  );
};

const DetailItem = ({ label, value }) => (
  <div className="flex items-center gap-2 mb-3">
    <h3 className="text-gray-300 capitalize font-semibold text-[18px]">{label}</h3>
    <p className="first-letter:uppercase text-gray-400">{value}</p>
  </div>
);

export default Detail;
