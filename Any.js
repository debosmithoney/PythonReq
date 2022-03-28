import axios from "axios";

const fetchData = () => {
  return axios
    .get("anyapi/")
    .then(({ data }) => {
      console.log(data);
      return data;
    })
    .catch((err) => {
      console.error(err);
    });
};

useEffect(() => {
  fetchData().then((randomData) => {
    setrandmData(JSON.stringify(randomData, null, 2));
  });
}, []);
