// Patent Generator Plugin Main Entry
// Accepts PDF, Word, or Markdown input, extracts invention details, performs prior art search, brainstorms, and generates Indian patent application draft.

const fs = require('fs');
const path = require('path');
const pdfParse = require('pdf-parse');
const mammoth = require('mammoth');
const { extractPatentInfo, assessPatentability, searchPriorArt, brainstormNovelty, scorePatentability, generateDraftTemplate, generatePatentApplication } = require('./lib/patentWorkflow');

async function processInput(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  let text = '';
  if (ext === '.pdf') {
    const dataBuffer = fs.readFileSync(filePath);
    const data = await pdfParse(dataBuffer);
    text = data.text;
  } else if (ext === '.docx') {
    const data = await mammoth.extractRawText({ path: filePath });
    text = data.value;
  } else if (ext === '.md') {
    text = fs.readFileSync(filePath, 'utf-8');
  } else {
    throw new Error('Unsupported file type. Please provide PDF, Word (.docx), or Markdown (.md) file.');
  }

  // 2. Extract information
  const extracted = extractPatentInfo(text);

  // 3. Assess patentability
  const assessment = assessPatentability(extracted);

  // 4. Prior art search
  const priorArt = await searchPriorArt(extracted);

  // 5. Brainstorming
  const brainstormed = await brainstormNovelty(extracted, priorArt);

  // 6. Scoring
  const score = scorePatentability(brainstormed, priorArt);

  // 7. Draft input template
  const draftTemplate = generateDraftTemplate(brainstormed);

  // 8. Generate patent application
  const patentDraft = generatePatentApplication(draftTemplate);

  return {
    extracted,
    assessment,
    priorArt,
    brainstormed,
    score,
    draftTemplate,
    patentDraft
  };
}

module.exports = { processInput };