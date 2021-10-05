img = tf.io.read_file();

async function run() {
  const MODEL_URL = "http://127.0.0.1:8887/JS-Model-2/model.json";
  const model = await tf.loadGraphModel(MODEL_URL);
  console.log(model.summary());
  //   const input = tf.tensor2d([10.0], [1, 1]);
  //   const result = model.predict(input);
  //   alert(result);
}
run();
