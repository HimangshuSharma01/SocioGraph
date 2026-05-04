<!DOCTYPE html>
<html>
<body>

  <!-- Header Section -->
  <div align="center">
    <h1>SocioGraph</h1>
    <p><strong>A High-Performance Social Network Analysis & Recommendation Engine</strong></p>
    <hr />
  </div>

  <!-- Project Overview -->
  <h3>Overview</h3>
  <p>
    SocioGraph is a Python-powered tool designed to simulate social media algorithms. It processes large-scale JSON datasets to find "People You May Know" based on mutual connections, while ensuring data integrity through a robust cleaning pipeline.
  </p>

  <!-- Key Features -->
  <h3>Key Features</h3>
  <ul>
    <li><strong>Smart Recommendations:</strong> Uses mutual friend counts to rank potential connections.</li>
    <li><strong>Data Sanitization:</strong> Automatically removes "ghost" accounts and fixes duplicate data.</li>
    <li><strong>Optimized Performance:</strong> Built with <code>Sets</code> and <code>Dictionaries</code> for $O(1)$ lookup speeds, making it capable of handling 10k+ users.</li>
    <li><strong>JSON Integration:</strong> Seamlessly reads and writes to raw data files.</li>
  </ul>

  <!-- Technical Breakdown -->
  <h3>Technical Stack</h3>
  <table border="1" style="width:100%; border-collapse: collapse; text-align: left;">
    <tr style="background-color: #f2f2f2;">
      <th style="padding: 8px;">Category</th>
      <th style="padding: 8px;">Technology</th>
    </tr>
    <tr>
      <td style="padding: 8px;">Language</td>
      <td style="padding: 8px;">Python 3.x</td>
    </tr>
    <tr>
      <td style="padding: 8px;">Data Format</td>
      <td style="padding: 8px;">JSON</td>
    </tr>
    <tr>
      <td style="padding: 8px;">Logic</td>
      <td style="padding: 8px;">Set Theory,List,Dict & Lambda Sorting</td>
    </tr>
  </table>

  <!-- How it Works Section -->
  <h3>How It Works</h3>
  <p>The recommendation logic follows a three-step graph traversal:</p>
  <ol>
    <li><strong>Clean:</strong> Removes users with empty names or zero activity.</li>
    <li><strong>Discover:</strong> Scans "friends-of-friends" while filtering out existing connections.</li>
    <li><strong>Rank:</strong> Sorts the results so the most relevant matches appear first.</li>
  </ol>

  <!-- Future Roadmap -->
  <h3>Future Roadmap</h3>
  <details>
    <summary>Click to view planned updates</summary>
    <ul>
      <li>Common interest matching using <code>liked_pages</code>.</li>
      <li>Data visualization </li>
      <li>Dataset of 1 Million users </li>
    </ul>
  </details>
</body>
</html>
