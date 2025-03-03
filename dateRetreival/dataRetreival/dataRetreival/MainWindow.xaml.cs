using Nest;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace dataRetreival
{
    public partial class MainWindow : Window
    {
        private static readonly string ElasticSearchUri = "http://localhost:9200";
        private static readonly string IndexName = "test-topic";
        private readonly ElasticClient _client;
        public MainWindow()
        {
            InitializeComponent();
            // Initialize Elasticsearch client
            var settings = new ConnectionSettings(new Uri(ElasticSearchUri))
                .DefaultIndex(IndexName);
            _client = new ElasticClient(settings);
        }
        private async void FetchData_Click(object sender, RoutedEventArgs e)
        {
            var searchResponse = await _client.SearchAsync<Data>(s => s
                .Index(IndexName)
                .Query(q => q.MatchAll())
                .Size(10000));

            if (!searchResponse.IsValid)
            {
                MessageBox.Show($"Error: {searchResponse.OriginalException?.Message}");
                return;
            }
            var machineDataList = searchResponse.Documents.ToList();
            dataGrid.ItemsSource = null;
            dataGrid.ItemsSource = machineDataList;
            dataGrid.Items.Refresh();
        }
    }
}