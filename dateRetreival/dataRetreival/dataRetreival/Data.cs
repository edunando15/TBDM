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
        public string Id { get; set; }

        [JsonProperty("id_macchina")]
        public string MachineId { get; set; }

        [JsonProperty("valore")]
        public double Value { get; set; }

        [JsonProperty("data_registrazione")]
        public DateTime RegistrationDate { get; set; }

        [JsonProperty("createdAt")]
        public DateTime CreatedAt { get; set; }

        [JsonProperty("updatedAt")]
        public DateTime UpdatedAt { get; set; }

        [JsonProperty("nome_parametro")]
        public string ParameterName { get; set; }

        [JsonProperty("tipo_dato")]
        public string DataType { get; set; }
    }

}
