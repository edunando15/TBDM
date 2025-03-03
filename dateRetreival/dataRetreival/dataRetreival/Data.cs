using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace dataRetreival
{
    public class Data
    {
        [JsonProperty("id")]
        public string id { get; set; }

        [JsonProperty("id_macchina")]
        public string id_macchina { get; set; }

        [JsonProperty("valore")]
        public double valore { get; set; }

        [JsonProperty("data_registrazione")]
        public DateTime data_registrazione { get; set; }

        [JsonProperty("createdAt")]
        public DateTime createdAt { get; set; }

        [JsonProperty("updatedAt")]
        public DateTime updatedAt { get; set; }

        [JsonProperty("nome_parametro")]
        public string nome_parametro { get; set; }

        [JsonProperty("tipo_dato")]
        public string tipo_data { get; set; }
    }

}
